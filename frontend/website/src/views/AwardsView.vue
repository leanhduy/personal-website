<template>
  <div class="container-fluid text-start">
    <section class="resume-section" id="awards">
      <div class="resume-section-content">
        <h2 class="mb-5">Awards & Certifications</h2>
        <ul class="fa-ul">
          <li class="mb-3" v-for="award in this.awards" :key="award.id">
            <span class="fa-li"
              ><i
                class="text-warning my-award-icon"
                :class="award.award_type === 'certification' ? 'fas fa-certificate' : 'fas fa-award'"
                style="font-size: 1.25rem"
              ></i
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
  name: 'AwardsView',
  setup() {
    const { awards, error, load } = getAwards()
    load()

    return { awards, error }
  },
}
</script>
