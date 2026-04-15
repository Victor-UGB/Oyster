from rest_framework import serializers

def validate_file_size(max_size, label):
    def validator(file):
        if file.size > max_size:
            raise serializers.ValidationError(
                f"{label} must not exceed {max_size // (1024 * 1024)}MB"
            )
        return file
    return validator