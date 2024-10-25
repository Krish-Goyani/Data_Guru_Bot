import re

class MessageFormatter:

    @staticmethod
    def format_gemini_response( text: str) -> str:
        """
        Format Gemini's response to Telegram-compatible markdown
        """
        # Replace Gemini's markdown with Telegram-compatible markdown
        formatted_text = text
        
        # Format headers (##) to bold text
        formatted_text = re.sub(r'^##\s+(.+)$', r'*\1*', formatted_text, flags=re.MULTILINE)
        
        # Format bold text (remove extra asterisks)
        formatted_text = re.sub(r'\*\*(.+?)\*\*', r'*\1*', formatted_text)
        
        # Format bullet points
        formatted_text = re.sub(r'^\*\s+', '• ', formatted_text, flags=re.MULTILINE)
        
        # Escape special characters that could interfere with markdown
        special_chars = ['_', '`', '[', ']', '(', ')', '~', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
        for char in special_chars:
            formatted_text = formatted_text.replace(char, '\\' + char)
        
        # Clean up any double escapes
        formatted_text = formatted_text.replace('\\\\', '\\')
        
        return formatted_text

    @staticmethod
    def ensure_markdown_entities_closed(text: str) -> str:
        """
        Ensure all markdown entities are properly closed in the text
        """
        # Count asterisks for bold/italic
        asterisk_count = text.count('*')
        if asterisk_count % 2 != 0:
            text = text.replace('*', '')  # Remove incomplete formatting
        
        return text

    @staticmethod
    def split_message(text: str, max_length: int = 4096) -> list[str]:
        """
        Split a message into chunks while preserving markdown formatting
        """
        text = MessageFormatter.format_gemini_response(text)
        messages = []
        current_text = text
        
        while current_text:
            if len(current_text) <= max_length:
                messages.append(MessageFormatter.ensure_markdown_entities_closed(current_text))
                break
            
            # Find a good splitting point
            split_index = current_text.rfind('\n', 0, max_length)
            if split_index == -1 or split_index < max_length // 2:
                split_index = current_text.rfind('. ', 0, max_length)
            if split_index == -1:
                split_index = max_length
            
            # Get the chunk and ensure markdown is properly closed
            chunk = current_text[:split_index]
            chunk = MessageFormatter.ensure_markdown_entities_closed(chunk)
            messages.append(chunk)
            
            # Prepare next chunk
            current_text = current_text[split_index:].lstrip()
            
            # If there are any unclosed markdown entities from the previous chunk,
            # we need to add them to the start of the next chunk
            if chunk.count('*') % 2 != 0:
                current_text = '*' + current_text
        
        return messages