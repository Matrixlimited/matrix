import axios from "axios";

const API_URL = "http://localhost:5000";
export interface LoginResponse {
  confirmation: string;
}
export interface VerificationResponse {}
export const Login = async (
  apiId: string,
  apiHash: string,
  phoneNumber: string
) => {
  try {
    const response = await axios.get<LoginResponse>(
      `${API_URL}/bot/create?api_id=${apiId}&api_hash=${apiHash}&phone_number=${phoneNumber}`
    );
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error("Error login", error);
    return null;
  }
};

export const Verification = async (s: string) => {
  try {
    const response = await axios.get<LoginResponse>(
      `${API_URL}/bot/code?verification_code=${s}`
    );
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error("Error login", error);
    return null;
  }
};
