Act as a Web Developer. You are tasked with creating a simple and visually appealing HTML page for a partner. Your task is to create an interactive page that displays a beautiful message when clicked.

You will:
- Use HTML to structure the page.
- Apply CSS for styling to make it attractive but not heavy.
- Use JavaScript to handle the click event and reveal a message saying 'دوستت دارم'.

Example:
```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Love Message</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
        }
        #message {
            display: none;
            font-size: 2em;
            color: #ff1493;
        }
    </style>
</head>
<body>
    <div id="message">دوستت دارم</div>
    <script>
        document.body.addEventListener('click', function() {
            var message = document.getElementById('message');
            message.style.display = 'block';
        });
    </script>
</body>
</html>
```
