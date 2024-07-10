import { useState, useContext } from "react";
import axios from "axios";

import ErrorPanel from "../../Components/ErrorPanel";

import APPCONTEXT from "../../Context/APPCONTEXT";

import { useNavigate } from "react-router-dom";

function SignUp() {
  const [alias, setAlias] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [eMsg, setEMsg] = useState(null);

  const { setUser, setToken } = useContext(APPCONTEXT);

  const navigate = useNavigate();

  const handleSubmit = () => {
    axios({
      method: "POST",
      url: "http://127.0.0.1:9000/signup",
      data: {
        alias: alias,
        email: email,
        password: password,
      },
    })
      .then((res) => {
        setEMsg(null);
        navigate("/");
      })
      .catch((e) => {
        setEMsg(e?.response?.data?.message || "Error Try Again");
      });
  };

  return (
    <div className=" c_screen">
      <div className="w3-panel w3-teal">
        <h3>SIGN UP</h3>
      </div>
      <div
        className=""
        style={{ display: "flex", justifyContent: "center", width: "100%" }}
      >
        <div
          className="w3-card-4 w3-padding"
          style={{
            width: "30%",
          }}
        >
          <label className="w3-text-blue">
            <b>Alias</b>
          </label>
          <input
            className="w3-input w3-border"
            type="text"
            onChange={(e) => setAlias(e.target.value)}
          />

          <label className="w3-text-blue">
            <b>Email</b>
          </label>
          <input
            className="w3-input w3-border"
            type="text"
            onChange={(e) => setEmail(e.target.value)}
          />

          <label className="w3-text-blue">
            <b>Passoword</b>
          </label>
          <input
            className="w3-input w3-border"
            type="password"
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            onClick={handleSubmit}
            style={{ marginTop: "10px" }}
            className="w3-btn w3-blue"
          >
            Sign Up
          </button>
        </div>
      </div>

      <ErrorPanel eMsg={eMsg} />
    </div>
  );
}

export default SignUp;
