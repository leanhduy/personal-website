<template>
  <div class="container-fluid text-start">
    <section class="resume-section" id="skills">
      <div class="resume-section-content">
        <h2 class="mb-5">Skills</h2>
        <div class="h3 mb-3">Programming Languages & Tools</div>
        <ul class="list-inline dev-icons">
          <li class="list-inline-item my-svg" v-for="skill in this.skills" :key="skill.id">
            <img class="my-skill-image" :src="`${MEDIA_URL}${skill.svg_image}`" alt="skill.name" />
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
import getSkills from '../composables/getSkills.js'
export default {
  name: 'SkillsView',
  setup() {
    const { skills, error, load } = getSkills()
    load()
    return { skills, error }
  },
  computed: {
    MEDIA_URL() {
      return process.env.VUE_APP_MEDIA_URL
    },
  },
}
</script>

<style scoped>
.my-skill-image {
  width: 4rem;
  height: 4rem;
  max-width: 4rem;
  object-fit: cover;
}
</style>
