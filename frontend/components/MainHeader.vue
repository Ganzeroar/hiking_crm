<template>
    <div>
        <nav class="navbar header has-shadow is-primary" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <a class="navbar-item" href="/">
                    <img src="~assets/logo.svg" />
                </a>
            </div>
            <div class="navbar-item header-phone">+7 (812) 628-52-98</div>
        </nav>
    </div>
</template>

<script>

export default {
    name: 'MainHeader',
}
</script>
<style scoped>
.navbar-brand {
    margin-left: 25rem;
}

.navbar {
    min-height: 5.35rem;
    background-color: #fff
}

.navbar-item img {
    max-height: 100%;
}

.header-phone {
    font-weight: 900 !important;
    font-size: 1.25rem !important;
}
</style>