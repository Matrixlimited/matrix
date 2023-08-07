import React, { useState } from "react";
import Button from "../components/Button";
import Input from "../components/Input";

interface InputFormProps {
  onSubmit: (apiId: string, apiHash: string, phoneNumber: string) => void;
}

const LoginForm: React.FC<InputFormProps> = ({ onSubmit }) => {
  const [apiId, setApiId] = useState("");
  const [apiHash, setApiHash] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(apiId, apiHash, phoneNumber);
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

      <Button type="submit">Login</Button>
    </form>
  );
};

export default LoginForm;
