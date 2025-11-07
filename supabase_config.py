from supabase import create_client, Client

url = "https://ckdzmsagzgainqkdgpwy.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNrZHptc2FnemdhaW5xa2RncHd5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI1NDU4ODgsImV4cCI6MjA3ODEyMTg4OH0.hfnXtuBa32Ibg9y9ZAsw0cXjBgsSn7cI2lJqWS6Vn_g"

supabase: Client = create_client(url, key)
