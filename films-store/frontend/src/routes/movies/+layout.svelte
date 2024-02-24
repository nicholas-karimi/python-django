<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a href="#" class="nav-brand">MovieApp</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggle-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                        <a href="/movies" class="nav-link">Movie List</a>
                </li>
                <li class="nav-item">
                    <a href="/movies/add" class="nav-link">Add Movie</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div class="container">
    <slot /> <!-- where pg element will be rendered -->
</div>