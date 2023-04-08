<template>
  <div class="container-fluid text-start">
    <section class="resume-section" id="awards">
      <div class="resume-section-content">
        <h2 class="mb-5">Awards & Certifications</h2>
        <ul class="fa-ul mb-0">
          <li v-for="award in this.awards" :key="award.id">
            <span class="fa-li"
              ><i class="text-warning" :class="award.type === 'certificate' ? 'fas fa-certificate' : 'fas fa-award'"></i
            ></span>
            {{ award.name }} - {{ new Date(award.date_taken).getFullYear() }}
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
import getAwards from '../composables/getAwards'
export default {
  name: 'HomeView',
  setup() {
    const { awards, error, load } = getAwards()
    load()
    return { awards, error }
  },
}
</script>
