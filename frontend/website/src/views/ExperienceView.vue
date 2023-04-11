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
            <div class="subheading mb-3">{{ exp.organization }}</div>
            <div class="subheading mb-3 text-info">Main Responsibilities</div>
            <ul>
              <li v-for="item in exp.responsibilities.split('\n')" :key="item">
                {{ item }}
              </li>
            </ul>
          </div>
          <div class="flex-shrink-0">
            <h5 class="text-primary">
              {{ new Date(exp.start_date).toLocaleString('default', { month: 'short', year: 'numeric' }) }}
              -
              {{ new Date(exp.end_date).toLocaleString('default', { month: 'short', year: 'numeric' }) }}
            </h5>
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
