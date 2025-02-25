<script>
	import Signup from './../../lib/signup.svelte';
	import Login from './../../lib/login.svelte';
    import { fade ,slide } from 'svelte/transition';
	

   
    

    let toggle = true;
</script>

<div class=" lg:w-3/12 m-auto mt-4 p-2 md: w-6/12 sm: w-10/12">
    <div class="w-full flex justify-between">
        <button class="w-1/2 p-2 transition duration-300 ease-in-out" 
            class:bg-amber-100={toggle} 
            class:bg-transparent={!toggle} 
            on:click={() => toggle = true}>
            Login
        </button>
        <button class="w-1/2 p-2 transition duration-300 ease-in-out" 
            class:bg-amber-100={!toggle} 
            class:bg-transparent={toggle} 
            on:click={() => toggle = false}>
            Signup
        </button>
    </div>

    <div class="overflow-hidden mt-4">
        {#key toggle}
        <div in:fade out:slide={{ duration: 400 }}>
            {#if toggle}
                <Login />
            {:else}
                <Signup />
            {/if}
        </div>
        {/key}
    </div>
</div>
