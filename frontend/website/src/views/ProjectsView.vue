<template>
  <div class="container-fluid text-start">
    <section class="resume-section" id="experience">
      <div class="resume-section-content">
        <h2 class="mb-5">Projects</h2>
        <div
          class="d-flex flex-column flex-md-row justify-content-between mb-5"
          v-for="project in this.projects"
          :key="project.id"
        >
          <div class="flex-grow-1">
            <h3 class="mb-0">{{ project.name }}</h3>
            <div class="subheading mb-3">
              <!-- TODO: Find way to fetching tag for every tag id of the Project object -->
            </div>
            <p>
              {{ project.description }}
            </p>
            <div class="social-icons">
              <a class="social-icon-sm" :href="project.source_url"><i class="fab fa-github"></i></a>
              <a class="social-icon-sm" :href="project.website_url"><i class="fa fa-globe"></i></a>
            </div>
          </div>
          <div class="container text-end">
            <img
              :src="`${MEDIA_URL}${project.featured_image}`"
              class="featured_image mt-2 rounded-pill"
              :alt="project.name"
            />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import getProjects from '../composables/getProjects.js'
export default {
  name: 'ProjectsView',
  setup() {
    const { projects, error, load } = getProjects()
    load()
    return { projects, error }
  },
  computed: {
    MEDIA_URL() {
      return process.env.VUE_APP_MEDIA_URL
    },
  },
}
</script>
<style scoped>
.featured_image {
  width: 20rem;
  height: 10rem;
  max-width: 25rem;
  object-fit: cover;
}
</style>
