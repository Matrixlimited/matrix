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
    command_to_execute = f"python login_script.py --phone {request.args.get('phone_number')} --id {int(request.args.get('api_id'))} --hash {request.args.get('api_hash')}"
    logger.error(command_to_execute)
    logger.error('Pokrecem')
    
    #process = pexpect.spawn(command_to_execute, encoding="utf-8")
    process = pexpect.spawn("/bin/sh -c '{}'".format(command_to_execute), encoding="utf-8")
    process.waitnoecho()
    #time.sleep(10)
    logger.error("POKRENUO")
    try:
        # Expecting the specific prompt from .py and respond accordingly
        # Phone number
        #phone_flag = process.expect([re.compile(r"Please enter your phone \(or bot token\): "), pexpect.EOF])
        #if phone_flag == 0:
        logger.error(request.args.get("phone_number"))
        process.sendline(str(request.args.get("phone_number")))
        process.waitnoecho()
        print("USPESNO")
        logger.error("uspesno")
        #if phone_flag == 1:
        # print("AAAA")
        # logger.error('aaaa')

        # Verification code
        #code_flag = process.expect([re.compile(r"Please enter the code you received: "), pexpect.EOF])
        # Start task for waiting verification code
        code_task = asyncio.create_task(wait_for_code_task())
        #if code_flag == 0:
        code = await code_task
        process.sendline(code)
        process.waitnoecho()
        logger.error("poslatooo")
        #elif code_flag == 1:
        # print("SKEKSTER")
        # logger.error("skekster")

        # Process the output from the subprocess
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

