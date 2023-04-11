<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top" id="sideNav">
    <a class="navbar-brand js-scroll-trigger" href="#page-top">
      <span class="d-block d-lg-none">Duy Le</span>
      <span class="d-none d-lg-block"
        ><img
          class="img-fluid img-profile rounded-circle mx-auto mb-2"
          src="assets/img/profile.png"
          alt="Duy Le's profile picture"
      /></span>
    </a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarResponsive"
      aria-controls="navbarResponsive"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarResponsive">
      <!-- TODO: REPLACE ALL HREF WITH ROUTER-LINKS  -->
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link class="nav-link js-scroll-trigger" :to="{ name: 'home' }">About</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link js-scroll-trigger" :to="{ name: 'projects' }">Projects</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link js-scroll-trigger" :to="{ name: 'experiences' }">Experience</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link js-scroll-trigger" :to="{ name: 'education' }">Education</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link js-scroll-trigger" :to="{ name: 'skills' }">Skills</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'awards' }">Awards</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {}
</script>

<style></style>
