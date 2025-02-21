<script>
    import axios from "axios";
    import { onMount } from "svelte";



let data=[]
const fetchdata=()=>{
    axios.get("http://127.0.0.1:8000/api/books")
    .then(res=>
      { console.log(res.data)
        data=res.data
      }
    ).catch(err=>
        console.log(err)
    )
}

const handeldelete=(id)=>{
    axios.delete(`http://127.0.0.1:8000/api/books/${id} `)
    .then(res=>
    console.log(res.data)
    ).catch(err=>
    console.log(err)
    )
}
onMount(()=>{
    fetchdata()
})
</script>
<div class ="w-10/12 m-auto ">
    <h1 class=" text-center text-xl m-3">ALL book</h1>
    <table class="table-auto w-full border-collapse mt-3">
        <thead>
            <tr class="border-1 p-2">
                <th class="border-1 p-2">Sr No</th>
                <th class="border-1 p-2">Book Name</th>
                <th class="border-1 p-2">Author</th>
                <th class="border-1 p-2">Price</th>
                <th class="border-1 p-2">Published Date</th>
                <th class="border-1 p-2">Action</th>
            </tr>
        </thead>
        <tbody>
            {#each data as item,i}
           
            <tr class="border-1 p-2 odd:bg-cyan-200 even:bg-amber-50">
                <td class="border-1 p-2">{i}</td>
                <td class="border-1 p-2">{item.title}</td>
                <td class="border-1 p-2">{item.author}</td>
                <td class="border-1 p-2">{item.price}</td>
                <td class="border-1 p-2">{item.published_date}</td>
                <td class="border-1 p-2">
                    
                    <button class="p-1 pl-3 pr-3 bg-green-500 text-amber-50 m-1 ml-2 mr-2 rounded-xl">Update</button>
                    <button class="p-1 pl-3 pr-3 bg-red-500 text-amber-50 m-1 ml-2 mr-2 rounded-xl" on:click={()=>handeldelete(item.id)}>Delete</button>

                </td>
                </tr>
            {/each}
        </tbody>
    </table>

</div>
