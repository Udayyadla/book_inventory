<script>
    import axios from "axios";
    import { onMount } from "svelte";
    import { preventDefault } from "svelte/legacy";


let showModal=false
let data=[]
let serach=""
let sortBy = "";
let updatedBookData={ title:"" , author:"" , published_date:"" , price:"" , id:""}
const fetchdata=()=>{
    axios.get("http://127.0.0.1:8000/api/books/")
    .then(res=>
      { console.log(res.data)
        data=res.data
      }
    ).catch(err=>
        console.log(err)
    )
}
function sortBooks() {
        if (sortBy === "asc") {
            data = [...data].sort((a, b) => a.price - b.price);
        } else if (sortBy === "desc") {
            data = [...data].sort((a, b) => b.price - a.price);
        }else{
            fetchdata()
        }
    }
const update=(book)=>{
   updatedBookData={...book}
   showModal=true
}
const updatedata=(id)=>{
    axios.patch(`http://127.0.0.1:8000/api/books/${id}/`,updatedBookData)
    .then(res=>{ console.log(res.data)
        fetchdata()
        alert("Book updated successfully")
        showModal=false
    })
.catch(err=>
console.log(err)
)
      

}
const handeldelete=(id)=>{
    axios.delete(`http://127.0.0.1:8000/api/books/${id}/`)
    .then(res=>{
    console.log(res.data)
    alert("Book Deleted Successfully")
    fetchdata()
}
    ).catch(err=>{
    console.log(err)

    }
    )
}
const handelsearch=()=>{
   axios .get(`http://127.0.0.1:8000/api/books/?search=${serach}`)
   .then(res=>{
    data=res.data
    console.log(data)
   })
   .catch(err=>{
    console.log(err)
   })

}
onMount(()=>{
    fetchdata()
})
</script>
<div class ="w-10/12 m-auto ">
    <h1 class=" text-center text-xl m-3">ALL book</h1>
    <div class=" w-full flex justify-between mt-3 mb-3">
    <div class="  flex justify-center ">
        <input bind:value={serach} placeholder="search" class="border-2 p-0.5 pl-2 mb-2 mt-2 rounded-2xl outline-0 focus:border-red-600 mr-3"/>
        <button class=" bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl" on:click={handelsearch}>search</button>
    </div>
    <div class=" text-center ">
        <select class="w-full border-2 text-center rounded-3xl p-2" bind:value={sortBy} on:change={sortBooks}>
            <option value="">Sort By Price</option> 
            <option value="asc">Ascending Order</option>
            <option value="desc">Descending Order</option>
        </select>
       
       
    </div>
</div>
    {#if data.length===0}
        <h1 class="text-2xl mt-5 text-center text-red-500">No Result Found</h1>
    {:else}
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
                <td class="border-1 p-2">{i+1}</td>
                <td class="border-1 p-2">{item.title}</td>
                <td class="border-1 p-2">{item.author}</td>
                <td class="border-1 p-2">{item.price}</td>
                <td class="border-1 p-2">{item.published_date}</td>
                <td class="border-1 p-2">
                    
                    <button class="p-1 pl-3 pr-3 bg-green-500 text-amber-50 m-1 ml-2 mr-2 rounded-xl" on:click={()=>update(item)}>Update</button>
                    <button class="p-1 pl-3 pr-3 bg-red-500 text-amber-50 m-1 ml-2 mr-2 rounded-xl" on:click={()=>handeldelete(item.id)}>Delete</button>

                </td>
                </tr>
            {/each}
          
        </tbody>
    </table>
    {/if}
    {#if showModal}
    <div class="fixed inset-0 flex items-center justify-center bg-opacity-30 backdrop-blur-md">
        <div class="bg-white p-6 rounded-lg shadow-lg w-1/3">
          <div class="w-full p-3 text-center">
              <h1 class="text-3xl font-bold">Update Book Information</h1>
          </div>
          <div class="w-12/12 m-auto mt-5 p-1 justify-center">
              
              <label>Book Name</label>
              <input placeholder="book name" type="text" bind:value={updatedBookData.title} class="w-full border-b-2 p-0.5 pl-2 mb-2 mt-2 outline-0 focus:border-red-600"/>
  
              <label>Author Name</label>
              <input placeholder="author name" type="text" bind:value={updatedBookData.author} class="w-full border-b-2 p-0.5 pl-2 mb-2 mt-2 outline-0 focus:border-red-600"/>
  
              <label>Published Date</label>
              <input placeholder="book published_date" type="date" bind:value={updatedBookData.published_date} class="w-full border-b-2 p-0.5 pl-2 mb-2 mt-2 outline-0 focus:border-red-600"/>
  
              <label>Price</label>
              <input placeholder="book price" min="1" type="number" bind:value={updatedBookData.price} class="w-full border-b-2 p-0.5 pl-2 mb-2 mt-2 outline-0 focus:border-red-600"/>
             <div class="w-full  mt-1 p-3 flex justify-between">
                <button class=" bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl" on:click={()=>updatedata(updatedBookData.id)}>Update</button>
                 <button class=" bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl" on:click={()=>{showModal=false}}>close</button>
             </div>
           
          </div>
        </div>
  </div>
  
  {/if}

</div>
