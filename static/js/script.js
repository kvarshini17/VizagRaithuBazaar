// VizagRaithuBazaar JavaScript

// Phone number validation
function validatePhone(phone) {
    const phoneRegex = /^[6-9]\d{9}$/;
    return phoneRegex.test(phone);
}

// OTP validation
function validateOTP(otp) {
    return /^\d{6}$/.test(otp);
}

// Form validation for phone login
document.addEventListener('DOMContentLoaded', function() {
    const phoneForm = document.querySelector('form[action*="login"]');
    if (phoneForm) {
        phoneForm.addEventListener('submit', function(e) {
            const phoneInput = document.querySelector('input[name="phone_number"]');
            if (phoneInput) {
                const phone = phoneInput.value.trim();
                if (!validatePhone(phone)) {
                    e.preventDefault();
                    alert('Please enter a valid 10-digit phone number starting with 6-9');
                    phoneInput.focus();
                }
            }
        });
    }

    // OTP form validation
    const otpForm = document.querySelector('form[action*="verify-otp"]');
    if (otpForm) {
        otpForm.addEventListener('submit', function(e) {
            const otpInput = document.querySelector('input[name="otp"]');
            if (otpInput) {
                const otp = otpInput.value.trim();
                if (!validateOTP(otp)) {
                    e.preventDefault();
                    alert('Please enter a valid 6-digit OTP');
                    otpInput.focus();
                }
            }
        });

        // Auto-move OTP digits (optional enhancement)
        const otpInput = document.querySelector('input[name="otp"]');
        if (otpInput) {
            otpInput.addEventListener('input', function(e) {
                if (this.value.length === 6) {
                    this.form.querySelector('button[type="submit"]').focus();
                }
            });
        }
    }

    // Add crop form validation
    const cropForm = document.querySelector('form[action*="add-crop"]');
    if (cropForm) {
        cropForm.addEventListener('submit', function(e) {
            const cropName = document.querySelector('input[name="crop_name"]').value.trim();
            const price = document.querySelector('input[name="price_per_kg"]').value;
            const quantity = document.querySelector('input[name="quantity"]').value;
            const location = document.querySelector('input[name="location"]').value.trim();

            if (!cropName || !price || !quantity || !location) {
                e.preventDefault();
                alert('All fields are required');
                return;
            }

            if (parseFloat(price) <= 0) {
                e.preventDefault();
                alert('Price must be greater than 0');
                return;
            }

            if (parseFloat(quantity) <= 0) {
                e.preventDefault();
                alert('Quantity must be greater than 0');
                return;
            }
        });
    }

    // Order quantity validation
    const orderForm = document.querySelector('form[action*="place"]');
    if (orderForm) {
        orderForm.addEventListener('submit', function(e) {
            const quantityInput = document.querySelector('input[name="quantity"]');
            if (quantityInput) {
                const quantity = parseFloat(quantityInput.value);
                const maxQuantity = parseFloat(quantityInput.max);

                if (quantity <= 0) {
                    e.preventDefault();
                    alert('Quantity must be greater than 0');
                    quantityInput.focus();
                    return;
                }

                if (quantity > maxQuantity) {
                    e.preventDefault();
                    alert(`Maximum available quantity is ${maxQuantity} kg`);
                    quantityInput.focus();
                    return;
                }
            }
        });

        // Calculate total price dynamically
        const quantityInput = document.querySelector('input[name="quantity"]');
        const pricePerKg = document.querySelector('#price-per-kg');
        const totalPrice = document.querySelector('#total-price');

        if (quantityInput && pricePerKg && totalPrice) {
            quantityInput.addEventListener('input', function() {
                const quantity = parseFloat(this.value) || 0;
                const price = parseFloat(pricePerKg.textContent);
                const total = quantity * price;
                totalPrice.textContent = total.toFixed(2);
            });
        }
    }

    // Confirmation for status updates
    const statusForms = document.querySelectorAll('form[action*="update-order"]');
    statusForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const status = this.querySelector('select[name="status"]').value;
            if (!confirm(`Are you sure you want to update status to "${status}"?`)) {
                e.preventDefault();
            }
        });
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('fade-in');
    });

    // Search functionality for marketplace
    const searchInput = document.querySelector('#crop-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const cropCards = document.querySelectorAll('.crop-card');

            cropCards.forEach(card => {
                const cropName = card.querySelector('.card-title').textContent.toLowerCase();
                const location = card.querySelector('.text-muted').textContent.toLowerCase();

                if (cropName.includes(searchTerm) || location.includes(searchTerm)) {
                    card.parentElement.style.display = 'block';
                } else {
                    card.parentElement.style.display = 'none';
                }
            });
        });
    }

    // Filter orders by status
    const statusFilter = document.querySelector('#status-filter');
    if (statusFilter) {
        statusFilter.addEventListener('change', function() {
            const selectedStatus = this.value;
            const orderRows = document.querySelectorAll('tbody tr');

            orderRows.forEach(row => {
                const status = row.querySelector('.status-badge').textContent.trim();

                if (selectedStatus === 'all' || status === selectedStatus) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    }

    // Refresh page every 30 seconds on tracking page (to see status updates)
    if (window.location.pathname.includes('/order/track/')) {
        setInterval(() => {
            location.reload();
        }, 30000);
    }
});

// Copy phone number to clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert('Phone number copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// Format currency
function formatCurrency(amount) {
    return '₹' + amount.toFixed(2);
}

// Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-IN', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Print functionality for orders
function printOrder(orderId) {
    window.print();
}

// Share functionality (if Web Share API is available)
function shareOrder(orderId, cropName) {
    if (navigator.share) {
        navigator.share({
            title: 'VizagRaithuBazaar Order',
            text: `Order for ${cropName} placed successfully!`,
            url: window.location.href
        }).catch(err => console.log('Error sharing:', err));
    } else {
        alert('Sharing not supported on this browser');
    }
}

// Initialize tooltips (if Bootstrap tooltips are used)
document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    if (typeof bootstrap !== 'undefined') {
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
});
