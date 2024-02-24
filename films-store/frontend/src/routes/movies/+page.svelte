<script>
    // let movies = 'The God Father'
    // let movies = [
    //     {id: 1, name: 'The God Father', director: 'Francis Ford Coppola'},
        
    // ]
    import "../../movie-store"
    import { MovieStore } from "../../movie-store";
    import { onDestroy } from "svelte";
    import {onMount } from 'svelte';

    // let movies = []
    let tags = []
    let selectedTag = '';

    // reactive filter
    // $: filteredMovies = selectedTag ? $MovieStore.filter(movie => movie.tags.includes(selectedTag)) : $MovieStore
    $: filterMovies = $MovieStore.filter(movie => selectedTag == '' || movie.tags.includes(selectedTag))

    // get tags from the $MovieStore
    let setTags = () => {
        let tagSet = new Set()
        $MovieStore.forEach(movie => {
            movie.tags.forEach(tag => {
                tagSet.add(tag)
            })
        })
        tags = Array.from(tagSet)
    }

    // const unsubscribe = MovieStore.subscribe(values => movies = values)

    // onDestroy(unsubscribe)

    let addMovie = () => MovieStore.update(prev => {
        let newMovie = {id: 11, name: 'The Boys', director: 'Nicholas Karimi'}
        // preserve exisitn store values and add new
        return [...prev, newMovie]
    })
    // fetch data from django api 
    
    onMount(async function(){
        // Fetch data only once
        if (!$MovieStore.length){
            const res = await fetch('http://127.0.0.1:8000/api/moviestore/v1/movies/')
            const data = await res.json()
            // console.log(data);
            MovieStore.set(data)
        }
        setTags()
    })

    // delete
    let handleDelete = ((id) =>{
        // console.log(id);
        // const res = await fetch(`http://127.0.0.1:8000/api/moviestore/v1/movies/${id}`)
        const endpoint = `http://127.0.0.1:8000/api/moviestore/v1/movies/${id}`
        fetch(endpoint, {method: 'DELETE'}).then(response => {
            if (response.status == 204){
                MovieStore.update(prev => prev.filter(movie => movie.id != id))
                //  delete rags associated with a movie
                setTags()
            }
        })


    })

</script>

<div>
    <h2 class="my-4">Movie List</h2>
    {#if selectedTag}
        <p class="my-4 text-info">Debugging: {selectedTag}</p>
    {/if}
    <!-- tags -->
    <div class="my-4">
        {#each tags as tag}
            <button class="btn btn-warning mx-1 mb-1 btn-sm" on:click={() => selectedTag = tag}>{tag}
            </button>
            <!-- <span class="badge badge-pill bg-warning mx-1">{tag}</span> -->
        {/each}
            <button class="btn btn-info mx-1 mb-1 btn-sm" on:click={() => selectedTag = ''}>All</button>

    </div>

    <div class="my-4 row">
        <!-- {#each $MovieStore as movie} -->
        {#each filterMovies as movie}
        <div class="col-12 col sm-6 col-md-4 mb-3">
            <div class="card w-100 h-100">
                <img src="{ movie.image }" alt="Movie" class="card-img-top" style="height: 300px; object-fit: cover;">
                <div class="card-body d-flex flex-column justify-content-between gap-4">
                    <div>
                        <h5 class="card-title">{ movie.title }</h5>
                        <small class="text-muted">Release Date: <strong>{ movie.release_date }</strong></small>
                        <p class="text-muted">Directed by <strong>{ movie.director }</strong></p>
                    </div>
                    <div>
                        <a href="/movies/{movie.id}" class="btn btn-warning">View</a>

                        <button on:click={() => handleDelete(movie.id)} class="btn btn-danger ml-2">
                            <i class="bi bi-trash"></i> &nbsp; Delete
                        </button>
                        <div class="mt-3">
                            {#each movie.tags as tag}
                                <span class="badge bg-warning me-1 mb-1">{tag}</span>
                            {/each}
                        </div>
                    </div>
                    
                </div>
            </div>
            
        </div>  
        {/each}
    </div>
</div>
<!-- Loop -->
<!-- <ol> -->
    <!-- {#each movies as movie} -->
    <!-- {#each $MovieStore as movie}
        <li>
            <a href="/movies/{movie.id}">{movie.name}</a>
            <span>({movie.director})</span>
        </li>
    {/each}
</ol> -->
<!-- <button type="button" on:click={ addMovie}>
    Add Movie
</button> -->
<!-- if statement 
{#if movies.startsWith('Th')}
    <p>{movies.toUpperCase()} Starts with T</p>
{:else}
    <p>Does not start with T</p>
{/if}
-->
<!-- <h1>{movies.toUpperCase()}</h1>

<style>
    h1{
        font-size: 40px;
        background-color: brown;
    }
</style> -->