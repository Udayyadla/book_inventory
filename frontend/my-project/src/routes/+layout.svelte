<script>
    import "../app.css"
    import { initializeStores } from "@skeletonlabs/skeleton";

    initializeStores();
</script>
<main>
    <div class=" w-full  p-2 bg-cyan-200 flex justify-around sticky top-0 left-0 ">
        <a href="/">All book</a>
        <a href="/addbook">Add Book</a>
        
    </div>
    <div class="flex justify-center items-center">
    <slot/>
</div>
</main>