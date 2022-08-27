<template>
    <header class="navbar">
        <nav>
            <div class="branding">
                <img src="../assets/logo.png" alt="">
            </div>
            <ul class="navigation">
                <li><router-link to="/admin-overview-financing-request">
                    Overview Financing Request
                </router-link></li>
                <li><router-link to="/view-financing-request">
                    View Financing Request
                </router-link></li>
                <li><router-link to="/list-client">
                    View Client List
                </router-link></li>
                <li><router-link to="/edit-client">
                    Edit Client List
                </router-link></li>
            </ul>

            <ul v-show="client" class="navigation">
                <li><router-link to="/view-tools">
                    Goldman Sachs Tools
                </router-link></li>
                <li><router-link to="/client-overview-financing-req">
                    View Financing Requests
                </router-link></li>
                <li><router-link to="/create-financing-request">
                    Create Financing Request
                </router-link></li>
            </ul>

        </nav>
    </header>
</template>

<style scoped>
    header {
        position: absolute;
        z-index: 99;
        nav {
            display: flex;
            flex-direction: row;
            padding: 12px 0;
        }
    }
</style>