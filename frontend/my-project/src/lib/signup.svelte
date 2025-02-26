<script>
	import Model from './model.svelte';
    import { goto } from "$app/navigation";
    import axios from "axios";

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
</script>
<div class="w-full p-2 mt-2">
    <from class="w-full mt-4">
        <label for="name"  class="text-xl">Name : </label>
        <input class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2"  type="text" bind:value={username} placeholder="Enter your username" required>

        <label for="name" class="text-xl">Email : </label>
        <input class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2" placeholder="Enter Email" type="text" bind:value={email} required>
       
        <label for="name" class="text-xl">Password : </label>
        <input class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2" placeholder="Enter Password" type="password" bind:value={password} required>
     

         <div class="flex justify-center">
            <button class="bg-blue-400 text-white font-bold py-2 px-4 rounded mt-3" on:click={()=>handlesignup()}>Signup</button>
         </div>
    </from>
   <Model isOpen={showModal} onClose={closeAlert} message={message} warning={warning}></Model> 
</div>