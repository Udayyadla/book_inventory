<script>
	import Model from './model.svelte';
    import { goto } from "$app/navigation";
    import axios from "axios";
  import { validateEmail, validateName, validatePassword, } from '$lib';

    let email=""
    let password=""
    let username=""
    let showModal=false
    let message=""
    let warning=false
    const closeAlert=()=>{
        showModal=false
    }

const handlesignup=()=>{
    if(email===""||password===""||username===""){
        showModal=true
        message="Please fill in all fields"
        warning=true

        }
        else{
            if(validateEmail(email)&&validatePassword(password)&&validateName(username)){
            const user={
                email:email,
                password:password,
                username:username
                }
                axios.post(`http://127.0.0.1:8000/api/auth/register/`,user)
                .then((response)=>{
                    console.log(response.data)
                    goto("/login")
                    })
                    .catch((error)=>{
                        console.log(error)
                        
                        })
                    }
                }
}
</script>
<div class="w-full p-2 mt-2">
    <from class="w-full mt-4">
        <label for="name"  class="text-xl">Name : </label>
        <input class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2"  type="text" bind:value={username} placeholder="Enter your username" required>
         {#if username!=="" &&!validateName(username)}
            <p class="text-center text-red-600  animate-pulse">Name must be +4 letters and contain alphabets</p>
         {/if}
        <label for="name" class="text-xl">Email : </label>
        <input class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2" placeholder="Enter Email" type="text" bind:value={email} required>
          {#if email!==""&&!validateEmail(email) }
        <p class="text-center text-red-500 animate-pulse">Enter valid email address</p> 
    {/if}
        <label for="name" class="text-xl">Password : </label>
        <input class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2" placeholder="Enter Password" type="password" bind:value={password} required>
         {#if password!="" &&!validatePassword(password) }
        <p class="text-center text-red-500 animate-pulse">
            Password must be 8+ chars, with uppercase, lowercase, and number. with one special char
        </p> 
    {/if}

         <div class="flex justify-center">
            <button class="bg-blue-400 text-white font-bold py-2 px-4 rounded mt-3" on:click={()=>handlesignup()}>Signup</button>
         </div>
    </from>
   <Model isOpen={showModal} onClose={closeAlert} message={message} warning={warning}></Model> 
</div>