<script>
export default {
    props: {
        placeholder: String,
        minFractionDigits: Number,
        type: String,
    },
};
</script>

<template>
    <div>
        <InputNumber
            v-if="type === 'string'"
            :placeholder="placeholder"
            :minFractionDigits="minFractionDigits"
        />
        <InputText v-else :placeholder="placeholder" />
    </div>
</template>

<style scoped>
</style>