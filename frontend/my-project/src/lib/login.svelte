<script>
  import { validateEmail, validatePassword } from "$lib";
  import Model from "./model.svelte";

  import axios from "axios";

  let message = "";
  let isopen = false;
  let warning = false;

  let email = "";
  let password = "";
  let otp = false;
  let otpCode = "";

  const onClose = () => {
    isopen = false;
  };

  const handlesendOTP = () => {
    if (email == "" || password == "") {
      warning = true;
      isopen = true;
      message = "fill all fields";
    } else {
        if(validateEmail(email)&&validatePassword(password)){
      let obj = {
        email: email,
        password: password,
      };
      axios
        .post(`http://127.0.0.1:8000/api/auth/login/`, obj)
        .then((response) => {
          console.log(response.data);

          otp = true;
          isopen = true;
          warning = false

          message = response.data.message
        })
        .catch((err) => {
          console.log(err.response.data.non_field_errors[0]);
          isopen = true;
          warning = true
          message = err.response.data.non_field_errors[0];
        });
        }
    }
  };
  const handlelogin = () => {
    if (email == "" || otpCode == "") {
      warning = true;
      isopen = true;
      message = "fill all fields";
    } else {
      if (validateEmail(email)) {
        let obj = {
          email: email,
          code: otpCode,
        };
        axios
          .post("http://127.0.0.1:8000/api/auth/verify-otp/", obj)
          .then((response) => {
            console.log(response.data);
            localStorage.setItem("token", response.data.access);

            window.location.href = "/";
          })
          .catch((error) => {
            console.log(error);
            isopen = true;
            warning = true;
            message = error.response.data.non_field_errors[0];
          });
      }
      else{
        warning = true;
        isopen = true;
        message = "Invalid credentials"
      }
    }

  };
</script>

<div class="w-full p-2 mt-2">
  <from class="w-full mt-4">
    <label for="name" class="text-xl">Email : </label>
    <input
      class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2"
      placeholder="Enter your email"
      type="text"
      bind:value={email}
      required
    />
    <!-- {#if !validateEmail(email) }
        <p class="text-center text-red-500">Enter valid email address</p> 
    {/if} -->

    {#if otp}
      <label for="name" class="text-xl">OTP : </label>
      <input
        class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2"
        placeholder="Enter your OTP"
        type="text"
        bind:value={otpCode}
        required
      />
      <div class="flex justify-center">
        <button
          class="bg-blue-400 text-white font-bold py-2 px-4 rounded mt-3"
          on:click={() => handlelogin()}>Login</button
        >
      </div>
    {:else}
      <label for="name" class="text-xl">Password : </label>
      <input
        class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2"
        placeholder="Enter your Password"
        type="password"
        bind:value={password}
        required
      />
      <!-- {#if !validatePassword(password) }
        <p class="text-center text-red-500">
            Password must be 8+ chars, with uppercase, lowercase, and number. with one special char
        </p> 
    {/if} -->

      <div class="flex justify-center">
        <button
          class="bg-blue-400 text-white font-bold py-2 px-4 rounded mt-3"
          on:click={() => handlesendOTP()}>Send OTP</button
        >
      </div>
    {/if}
  </from>
  <Model {onClose} {message} {warning} isOpen={isopen}></Model>
</div>
