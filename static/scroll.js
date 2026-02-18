// Mobile-only scroll reveal
if (window.innerWidth <= 768) {

    const cards = document.querySelectorAll(".card");

    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("active");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.15 }
    );

    cards.forEach(card => observer.observe(card));
}
