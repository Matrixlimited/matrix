import axios from "axios";
//0.0.0.0:5000
const API_URL = "http://localhost:5000";
export interface LoginResponse {
  status: string;
}
export interface VerificationResponse {}
export const Login = async (
  apiId: string,
  apiHash: string,
  phoneNumber: string,
  sourceGroup: string,
  letterKey: string,
  offset: string
) => {
  try {
    const response = await axios.get<LoginResponse>(
      `${API_URL}/bot/create?api_id=${apiId}&api_hash=${apiHash}&phone_number=${phoneNumber}&source_group=${sourceGroup}&letter_key=${letterKey}&offset=${offset}`
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
