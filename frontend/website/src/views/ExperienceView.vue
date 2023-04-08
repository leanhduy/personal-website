<template>
  <div class="container-fluid text-start">
    <section class="resume-section" id="experience">
      <div class="resume-section-content">
        <h2 class="mb-5">Experience</h2>
        <div
          class="d-flex flex-column flex-md-row justify-content-between mb-5"
          v-for="exp in this.experiences"
          :key="exp.id"
        >
          <div class="flex-grow-1">
            <h3 class="mb-0">{{ exp.position }}</h3>
            <div class="subheading mb-3">{{ exp.company }}</div>
            <div class="subheading mb-3 text-info">Main Responsibilities</div>
            <ul>
              <li v-for="item in exp.responsibilities" :key="item">{{ item }}</li>
            </ul>
          </div>
          <div class="flex-shrink-0">
            <span class="text-primary">{{ exp.startDate }} - {{ exp.endDate }}</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import getExperiences from '../composables/getExperiences.js'
export default {
  name: 'ExperienceView',
  setup() {
    const { experiences, error, load } = getExperiences()
    load()
    return { experiences, error }
  },
}
</script>
<style scoped>
.featured_image {
  width: 50%;
  height: auto;
  object-fit: cover;
}
</style>
