<template>
  <div>
    <span>
      {{ $route.params.text }}
    </span>
    <router-link :to="{ name: 'proptest2', params: { prop1: 'huge11', prop2: 'tsuchida'} }" >
      link2
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    prop1: {
      type: String,
      require: true
    }
  }
}
</script>