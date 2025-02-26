<script>
    import Login from "./../lib/login.svelte";
    import "../app.css";
    import { initializeStores } from "@skeletonlabs/skeleton";
    import { onMount } from "svelte";
    import axios from "axios";

    initializeStores();
    let token = "";
    const logout=()=>{
        axios.post(`http://127.0.0.1:8000/api/auth/logout/`,{
            headers: {
                'Authorization': `Bearer ${token}`,
                }
        })
        .then(response => {
            console.log(response);
            token = "",
            window.location.href = "/login"
            localStorage.setItem("token",token)
            })
            .catch(error => {
                console.error(error);
                });
    }
    onMount(() => {
        token = localStorage.getItem("token") ?? "";
        console.log("Token loaded:", token);
    });

</script>

<main>
    <div
        class=" w-full p-2 bg-cyan-200 flex justify-around sticky top-0 left-0"
    >
        <a href="/">All book</a>
        <a href="/addbook">Add Book</a>
        <a href="/login">
            {#if token !== ""}
                <button on:click={logout}>Logout</button>
            {:else}
                <button>Login</button>
            {/if}
        </a>
    </div>
    <div class="flex justify-center items-center">
        <slot />
    </div>
</main>
