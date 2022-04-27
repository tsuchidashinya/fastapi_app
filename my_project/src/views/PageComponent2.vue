<template>
  <span>
    {{ prop1 }}
    {{ prop2 }}
  </span>
</template>

<script>
export default {
  props: {
    prop1: {
      type: String,
      default: ''
    },
    prop2: {
      type: String,
      require: true
    }
  }
}
</script>