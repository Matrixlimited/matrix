import asyncio
import pexpect
import logging
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask("telebot")
CORS(app)
verification_code = None


async def wait_for_code_task():
    global verification_code
    while verification_code is None:
        await asyncio.sleep(2)
    return verification_code


@app.route("/bot/create", methods=["GET"])
async def create_bot():
    global verification_code
    logger = logging.getLogger('tele')
    logger.setLevel(logging.DEBUG)
    command_to_execute = f"python login_script.py --phone {request.args.get('phone_number')} --id {int(request.args.get('api_id'))} --hash {request.args.get('api_hash')} --source_group {request.args.get('source_group')} --letter_key {request.args.get('letter_key')} --offset {int(request.args.get('offset'))}"
    logger.error(command_to_execute)
    logger.error('Pokrecem')
    
    #process = pexpect.spawn(command_to_execute, encoding="utf-8")
    process = pexpect.spawn("/bin/sh -c '{}'".format(command_to_execute), encoding="utf-8")
    process.waitnoecho()
    #time.sleep(10)
    logger.error("POKRENUO")
    try:
        logger.error(request.args.get("phone_number"))
        process.sendline(str(request.args.get("phone_number")))
        process.waitnoecho()
        print("USPESNO")
        logger.error("uspesno")
        code_task = asyncio.create_task(wait_for_code_task())
        #if code_flag == 0:
        code = await code_task
        process.sendline(code)
        process.waitnoecho()
        logger.error("poslatooo")
        print(process.before, end='')
        print("KRAJ USPESNOOO")

    except Exception as e:
        print(e)
    # Wait for the subprocess to finish
    process.wait()
    verification_code = None
    return jsonify(status="Logged in successfully")


@app.route("/bot/code", methods=["GET"])
def submit_code():
    global verification_code
    verification_code = request.args.get('verification_code')
    return jsonify(status="Code submitted successfully")


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

