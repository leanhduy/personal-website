<template>
  <div class="container-fluid p-0 text-start">
    <section v-if="this.profile" class="resume-section" id="about">
      <div class="resume-section-content">
        <h1 class="mb-0">
          {{ this.profile.firstname }}
          <span class="text-primary">{{ this.profile.lastname }}</span>
        </h1>
        <div class="subheading mb-1">
          {{ this.profile.location }}
        </div>
        <div class="subheading mb-1">
          <a :href="`mailto:${this.profile.email}`">{{ this.profile.email }}</a>
        </div>
        <p class="lead mb-5">
          {{ this.profile.bio }}
        </p>
        <div class="social-icons">
          <a class="social-icon" :href="this.profile.linkedin"><i class="fab fa-linkedin-in"></i></a>
          <a class="social-icon" :href="this.profile.github"><i class="fab fa-github"></i></a>
          <a class="social-icon" :href="this.profile.website"><i class="fa fa-globe"></i></a>
          <a class="social-icon" :href="this.profile.facebook"><i class="fab fa-facebook-f"></i></a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import getProfile from '../composables/getProfile.js'
export default {
  name: 'About',
  setup() {
    const { profile, error, load } = getProfile()
    load()
    return { profile, error }
  },
}
</script>

<style></style>
