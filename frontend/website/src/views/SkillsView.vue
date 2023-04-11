<template>
  <div class="container-fluid text-start">
    <section class="resume-section" id="skills">
      <div class="resume-section-content">
        <h2 class="mb-5">Skills</h2>
        <div class="subheading mb-3">Programming Languages & Tools</div>
        <ul class="list-inline dev-icons">
          <li class="list-inline-item my-svg" v-for="skill in this.skills" :key="skill.id">
            <object
              class="my-svg"
              :data="`assets/svg/${skill.svg_name}`"
              width="50"
              height="50"
              type="image/svg+xml"
            ></object>
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
}
</script>
