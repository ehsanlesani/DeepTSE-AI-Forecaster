<?php
// Set content type and encoding
header("Content-Type: text/html; charset=UTF-8");

// Optional: define path to HTML file
$html_file = 'index.html';

// Check if file exists
if (file_exists($html_file)) {
    // Load and display the HTML content
    readfile($html_file);
} else {
    echo "<h2>⚠️ Error: HTML file not found.</h2>";
}
?>
