<template>
  <div class="container-fluid text-start">
    <section class="resume-section" id="education">
      <div class="resume-section-content" v-for="ed in this.education" :key="ed.id">
        <h2 class="mb-5">Education</h2>
        <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
          <div class="flex-grow-1">
            <h3 class="mb-0 text-info">{{ ed.school_name }}</h3>
            <div class="subheading mb-3">{{ ed.degree }}</div>
            <div>Major: {{ ed.major }}</div>
            <p>GPA: {{ ed.gpa }}/10</p>
          </div>
          <div class="flex-shrink-0">
            <h4 class="text-primary">
              {{ new Date(ed.start_date).getMonth() }}/{{ new Date(ed.start_date).getFullYear() }} -
              {{ new Date(ed.end_date).getMonth() }}/{{ new Date(ed.end_date).getFullYear() }}
            </h4>
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
