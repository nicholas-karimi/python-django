<script>
    import { MovieStore } from "../../../movie-store";
    import { onMount } from 'svelte';


    export let data

    let movie;

    onMount(async function(){
        if ($MovieStore.length){
            movie = $MovieStore.find(movie => movie.id == data.id)
            console.log(movie);
        }
        else{
            const res = await fetch('http://127.0.0.1:8000/api/moviestore/v1/movies/{data.id}')
            if(res.status == 200){
                movie = await res.json()
                console.log(movie);
            } else {
                movie = null;
            }
        }
    })
</script>

<!-- <h1>{ data.movie.name }</h1>
<h1>{ data.movie.director }</h1>
<h1>{ data.movie.id }</h1> -->

<div class="row mt-4">
    {#if movie}
    <h2 class="mb-4">{ movie.title }</h2>
    <div class="col-12 col-md-4">
        <img src="{ movie.image }" alt="{ movie.title }" class="w-100">
    </div>
    <div class="col-12 col-md-8">
        <p class="mb-2"><b>{ movie.title }</b>, directed by <i>{ movie.director }</i></p>
        <p class="mb-2">Release Date: <strong>{ movie.release_date }</strong></p>
        <hr>
        <p class="mb-2">{ movie.description }</p>

        <a href="/movie/{movie.id}/update" class="btn btn-warning mt-2">Update</a>

    </div>
    {:else}
        <p>Movie not found with ID {data.id}</p>
    {/if}
</div>
