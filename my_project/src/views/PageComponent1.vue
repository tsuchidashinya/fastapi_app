<template>
  <span>
    {{ prop1 }}
  </span>
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