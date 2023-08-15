import React, { useState } from "react";
import Button from "../components/Button";
import Input from "../components/Input";
import { off } from "process";

interface InputFormProps {
  onSubmit: (
    apiId: string,
    apiHash: string,
    phoneNumber: string,
    sourceGroup: string,
    letterKey: string,
    offset: string
  ) => void;
}

const LoginForm: React.FC<InputFormProps> = ({ onSubmit }) => {
  const [apiId, setApiId] = useState("");
  const [apiHash, setApiHash] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [sourceGroup, setSourceGroup] = useState("");
  const [letterKey, setLetterKey] = useState("");
  const [offset, setOffset] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(apiId, apiHash, phoneNumber, sourceGroup, letterKey, offset);
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-5">
      <div className="flex flex-col gap-2">
        <label htmlFor="apiId">API ID:</label>
        <Input
          type="string"
          id="apiId"
          value={apiId}
          required
          onChange={(e) => setApiId(e.target.value)}
        />
      </div>

      <div className="flex flex-col gap-2">
        <label htmlFor="apiHash">API Hash:</label>
        <Input
          type="text"
          id="apiHash"
          value={apiHash}
          required
          onChange={(e) => setApiHash(e.target.value)}
        />
      </div>

      <div className="flex flex-col gap-2">
        <label htmlFor="phoneNumber">Phone Number:</label>
        <Input
          type="text"
          id="phoneNumber"
          value={phoneNumber}
          required
          onChange={(e) => setPhoneNumber(e.target.value)}
        />
      </div>
      <div className="flex flex-col gap-2">
        <label htmlFor="sourceGroup">Source Group:</label>
        <Input
          type="text"
          id="sourceGroup"
          value={sourceGroup}
          required
          onChange={(e) => setSourceGroup(e.target.value)}
        />
      </div>
      <div className="flex flex-col gap-2">
        <label htmlFor="letterKey">Letter Key:</label>
        <Input
          type="text"
          id="letterKey"
          value={letterKey}
          required
          onChange={(e) => setLetterKey(e.target.value)}
        />
      </div>
      <div className="flex flex-col gap-2">
        <label htmlFor="offset">Offset:</label>
        <Input
          type="text"
          id="offset"
          value={offset}
          required
          onChange={(e) => setOffset(e.target.value)}
        />
      </div>

      <Button type="submit">Login</Button>
    </form>
  );
};

export default LoginForm;
