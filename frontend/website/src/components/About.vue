<template>
  <div class="container-fluid p-0 text-start">
    <section v-if="profile" class="resume-section" id="about">
      <div class="resume-section-content">
        <h1 class="mb-0">
          {{ profile.name.split(' ')[0] }}
          <span class="text-primary">{{ profile.name.split(' ')[1] }}</span>
        </h1>
        <div class="subheading mb-1">
          {{ profile.location }}
        </div>
        <div class="subheading mb-1">
          <a :href="`mailto:${profile.email}`">{{ profile.email }}</a>
        </div>
        <div class="lead mb-5">
          <!-- {{ profile.bio }} -->
          <p v-for="item in profile.bio.split('\n')" :key="item">{{ item }}</p>
        </div>
        <div class="social-icons">
          <a class="social-icon" :href="profile.linkedin_profile"><i class="fab fa-linkedin-in"></i></a>
          <a class="social-icon" :href="profile.github_profile"><i class="fab fa-github"></i></a>
          <a class="social-icon" :href="profile.website_url"><i class="fa fa-globe"></i></a>
          <a class="social-icon" :href="profile.facebook_profile"><i class="fab fa-facebook-f"></i></a>
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
