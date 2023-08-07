import React, { useState } from "react";
import Button from "../components/Button";
import Input from "../components/Input";

interface InputFormProps {
  onSubmit: (verificationCode: string) => void;
}

const VerificationForm: React.FC<InputFormProps> = ({ onSubmit }) => {
  const [verificationCode, setVerificationCode] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(verificationCode);
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-5">
      <div className="flex flex-col gap-2">
        <label htmlFor="apiHash">Verification Code:</label>
        <Input
          type="text"
          id="apiHash"
          value={verificationCode}
          required
          onChange={(e) => setVerificationCode(e.target.value)}
        />
      </div>

      <Button type="submit">Confirm</Button>
    </form>
  );
};

export default VerificationForm;
