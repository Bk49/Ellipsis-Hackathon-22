<script>
import BaseFormFields from "./BaseFormFields.vue";

export default {
    props: {
        formFields: Array,
        submitFunction: Function,
        cancelFunction: Function,
    },
};
</script>

<template>
    <div>
        <BaseFormFields
            v-for="(item, index) in formFields"
            :placeholder="item.placeholder"
            :key="index"
            :v-model="item.vModel"
            :minFractionDigits="item.minFractionDigits"
            :type="item.type"
        />

        <Button label="Submit" @click="submitFunction()" />
        <Button
            v-if="cancelFunction"
            label="Cancel"
            @click="cancelFunction()"
        />
    </div>
</template>
