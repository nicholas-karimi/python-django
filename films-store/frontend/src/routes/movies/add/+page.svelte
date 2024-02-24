<script>
    import { MovieStore } from "../../../movie-store";
    import {goto} from '$app/navigation';

    let title = '';
    let description = '';
    let director = '';
    let files;
    let release_date = '';
    let tags = '';
    let showInvalidMessage = false;

    let validFields = () => {
        return title.length > 4 && director.length > 4 && description.length > 100;
    }

    // form subit
    let handleSubmit = () => {
        if(!validFields()){
            showInvalidMessage = true;
            return
        }
        // add data to the store
        // MovieStore.update(prev => {
        //     let id = prev[prev.length - 1].id + 1
        //     let newMovie = {id: id, name, director}
        //     return [...prev, newMovie]
        // })

        // use endpoint to post dat to db 
        const endpoint = "http://127.0.0.1:8000/api/moviestore/v1/movies/";
        let data = new FormData();
        data.append("title", title);
        data.append("description", description);
        data.append("director", director);
        data.append("image", files[0]);
        data.append("release_date", release_date);

        // check if there are tags and split them before saving
        if (tags.length) {
            let tagList = tags.split(",");
            // tagList.forEach(tag => data.append("tags", tag));
            // trim trailing white space 
            tagList.forEach(tag => data.append("tags", tag.trim()));
            }
        
        fetch(endpoint, { method: "POST", body: data }).then(response => response.json()).then(data => {
            // console.log(data);
            MovieStore.update(prev => [...prev, data])
            // redirect to
            goto("/movies")
        })
        // fetch(endpoint, {
        //     method: "POST",
        //     body: data,
        // }).then(response => response.json()).then(data => {
        //     // console.log(data);
        //     MovieStore.update(prev => {
        //         return [...prev, data]
        //         // [...prev, data]
        //     })
        //     // redirect to
        //     goto("/movies")
        // })
        
    }
</script>

<div>
    <h2 class="my-4">Add Movie</h2>

    {#if showInvalidMessage}
        <div class="alert alert-danger" role="alert">
            Please fill out all fields
        </div>
    {/if}
        <form on:submit|preventDefault={handleSubmit}>
                <div class="row">
                    <div class="col-md-6">
                        <label for="name" class="form-control-label">Movie Title</label>
                        <input type="text" class="form-control" placeholder="title" bind:value={title}>
                    </div>
                    <div class="col-md-6">
                        <label for="director" class="form-control-label">Movie Director</label>
                        <input type="text"  class="form-control"placeholder="director" bind:value={director}>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <label for="description" class="form-control-label">Movie Description</label>
                        <input type="text" class="form-control" placeholder="description" bind:value={description}>
                    </div>
                    <div class="col-md-6">
                        <label for="description" class="form-control-label">Movie Tags</label>
                        <input type="text" class="form-control" placeholder="tags" bind:value={tags}>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <label for="date" class="form-control-label">Movie Release Date</label>
                        <input type="date"  class="form-control" placeholder="release_date" bind:value={release_date}>
                    </div>
                    <div class="col-md-6">
                        <label for="image" class="form-control-label">Movie Image Poster</label>
                        <input type="file"  class="form-control" bind:files>
                    </div>
                </div>

                <div>
                    <button class="btn btn-primary btn-lg mt-3 float-end" type="submit">Add</button>
                </div>
        </form>
</div>


<style>
    .submit {
        background-color: blue !important;
        color: white;
        padding: 5px;
        border-radius: 10%;
        cursor:pointer;
        margin-top: 10px;
    }
    .submit:hover{
        transform: scale(100%);
    }
</style>