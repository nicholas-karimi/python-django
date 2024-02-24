<script>
  import { MovieStore } from "../../../../movie-store";
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";

  let title = "";
  let description = "";
  let director = "";
  let files;
  let release_date = "";
  let showInvalidMessage = false;
  export let data;
  let id;

  let validFields = () => {
    return title.length > 4 && director.length > 4 && description.length > 100;
  };

  // form subit
  let handleSubmit = () => {
    if (!validFields()) {
      showInvalidMessage = true;
      return;
    }
    // add data to the store
    // MovieStore.update(prev => {
    //     let id = prev[prev.length - 1].id + 1
    //     let newMovie = {id: id, name, director}
    //     return [...prev, newMovie]
    // })

    // use endpoint to post dat to db
    const endpoint = `http://127.0.0.1:8000/api/moviestore/v1/movies/${id}/`;
    let data = new FormData();
    data.append("title", title);
    data.append("description", description);
    data.append("director", director);
    // avoid filed being overwritten on update
    if (files) {
      data.append("image", files[0]);
    }
    data.append("release_date", release_date);

    fetch(endpoint, { method: "PUT", body: data })
      .then((response) => response.json())
      .then((data) => {
        // console.log(data);
        MovieStore.update((prev) => {
          let updatedMovies = $MovieStore.slcie();
          let index = updatedMovies.findIndex((movie) => movie.id == data.id);
          updatedMovies[index] = data;
          return updatedMovies;
        });
      });

    // redirect to
    goto("/movies");
  };

  onMount(async function () {
    id = data.id;
    let movie = {};
    if ($MovieStore.length) {
      movie = $MovieStore.find((movie) => movie.id == id);
      console.log(movie);
    } else {
      const res = await fetch(
        `http://127.0.0.1:8000/api/moviestore/v1/movies/${data.id}/`
      );
      if (res.status == 200) {
        movie = await res.json();
        console.log(movie);
      } else {
        movie = null;
      }
    }
    ({ title, description, director, release_date } = movie);
  });
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
        <input
          type="text"
          class="form-control"
          placeholder="title"
          bind:value={title}
        />
      </div>
      <div class="col-md-6">
        <label for="director" class="form-control-label">Movie Director</label>
        <input
          type="text"
          class="form-control"
          placeholder="director"
          bind:value={director}
        />
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <label for="description" class="form-control-label"
          >Movie Description</label
        >
        <input
          type="text"
          class="form-control"
          placeholder="description"
          bind:value={description}
        />
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <label for="date" class="form-control-label">Movie Release Date</label>
        <input
          type="date"
          class="form-control"
          placeholder="release_date"
          bind:value={release_date}
        />
      </div>
      <div class="col-md-6">
        <label for="image" class="form-control-label">Movie Image Poster</label>
        <input type="file" class="form-control" bind:files />
      </div>
    </div>

    <div>
      <button class="btn btn-primary btn-lg mt-3 float-end" type="submit"
        >Add</button
      >
    </div>
  </form>
</div>

<style>
  .submit {
    background-color: blue !important;
    color: white;
    padding: 5px;
    border-radius: 10%;
    cursor: pointer;
    margin-top: 10px;
  }
  .submit:hover {
    transform: scale(100%);
  }
</style>
