<script>
	import { fade ,fly} from 'svelte/transition';
    export let message = "This is an alert!";
    export let isOpen = true;
    export let onClose = () => {};
    export let warning=false
</script>

{#if isOpen}
    <div class="w-3/12 fixed bottom-0 right-0  flex items-bottom justify-end bg-transparent bg-opacity-50 animate-bounce in:fade"
    in:fade={{ duration: 300 }}
    out:fly={{ y: 20, duration: 300 }}
    >
        <div class=" w-full p-6 rounded-lg shadow-lg text-center {warning?"bg-red-400": "bg-blue-400"}">
            <p class="text-lg font-medium">{message}</p>
            <button on:click={onClose} class="mt-4 px-4 py-2 bg-white rounded-lg hover:bg-blue-100 transition">
                OK
            </button>
        </div>
    </div>
{/if}
