<template>
  <div class="container-fluid text-start">
    <section class="resume-section" id="education">
      <div class="resume-section-content" v-for="ed in this.education" :key="ed.id">
        <h2 class="mb-5">Education</h2>
        <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
          <div class="flex-grow-1">
            <h3 class="mb-0">{{ ed.school }}</h3>
            <div class="subheading mb-3">{{ ed.degree }}</div>
            <div>Major: {{ ed.major }}</div>
            <p>GPA: {{ ed.gpa }}</p>
          </div>
          <div class="flex-shrink-0">
            <span class="text-primary">{{ ed.startDate }} - {{ ed.endDate }}</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import getEducation from '../composables/getEducation.js'
export default {
  name: 'EducationView',
  setup() {
    const { education, error, load } = getEducation()
    load()
    return { education, error }
  },
}
</script>
