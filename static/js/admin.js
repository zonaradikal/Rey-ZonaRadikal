let latestUser = 0;
let latestSession = 0;

async function checkUpdates() {
    const response =
        await fetch("/admin/check-updates");
    const data =
        await response.json();

    if (
        latestUser !== 0 &&
        (
            data.latest_user > latestUser ||
            data.latest_session > latestSession
        )
    ) {
        location.reload();
    }

    latestUser = data.latest_user;
    latestSession = data.latest_session;
}

async function loadPendingCount() {
    try {
        const response =
            await fetch("/admin/pending-count");
        const data =
            await response.json();
        const badge =
            document.getElementById(
                "PendingBadge"
            );

        if (!badge) return;
        badge.textContent =
            data.count;
        badge.style.display =
            data.count > 0
                ? "flex"
                : "none";
    }

    catch(error) {
        console.error(error);
    }

}


document.addEventListener(
    "DOMContentLoaded",
    () => {
        checkUpdates();
        loadPendingCount();
        setInterval(
            checkUpdates,
            5000
        );
        setInterval(
            loadPendingCount,
            5000
        );
    }
);