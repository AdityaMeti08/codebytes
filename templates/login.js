import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.3/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/10.12.3/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCqFuMQs0m6l3k1T4u7o8zCq5EhX4lTkMs",
  authDomain: "codebyte-agri.firebaseapp.com",
  projectId: "codebyte-agri",
  storageBucket: "codebyte-agri.appspot.com",
  messagingSenderId: "172300657391",
  appId: "1:172300657391:web:401b7244cd2221fe64b11a",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();

const submit = document.getElementById("submit");
submit.addEventListener("click", function (e) {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      // Signed up
      const user = userCredential.user;
      alert("Login successful");
      window.location.href="main.py";
      // ...
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      alert(errorMessage);
      // ..
    });
});
