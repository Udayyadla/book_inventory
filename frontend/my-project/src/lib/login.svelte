
<script>
    import axios from "axios";

    let username=""
    let password=""

    const handlelogin=()=>{
        let obj={
            username:username,
            password:password
        }
        axios.post(`http://127.0.0.1:8000/api/token/`,obj)
        .then((response)=>{
            console.log(response.data)
            localStorage.setItem("token",response.data.access)
            alert("login success")
            window.location.href="/"
            })
            .catch((error)=>{
                console.log(error)
                alert("login failed")
                })
    }
</script>
<div class="w-full p-2 mt-2">
    <from class="w-full mt-4" on:submit={handlelogin}>
        <label for="name" class="text-xl">Email : </label>
        <input class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2" placeholder="Enter username" type="text" bind:value={username} required>
       
        <label for="name" class="text-xl">Password : </label>
        <input class="w-full border-1 rounded-2xl p-1 focus:border-red-600 pl-5 mb-2 mt-2" placeholder="Enter Password" type="password" bind:value={password} required>
     

         <div class="flex justify-center">
            <button class="bg-red-400 text-white font-bold py-2 px-4 rounded mt-3" type="submit">Login</button>
         </div>
    </from>
</div>