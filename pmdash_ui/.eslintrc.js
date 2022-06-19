module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: [
    'plugin:vue/base',
    'plugin:vue/vue3-strongly-recommended',
    'plugin:vue/vue3-recommended',
    'plugin:vue/vue3-essential',
    'plugin:vue/recommended',
    'prettier',
  ],
  parser: '@typescript-eslint/parser',
  ignorePatterns: ['node_modules/'],
  rules: {
    'vue/no-unused-vars': 'error',
  },
};
