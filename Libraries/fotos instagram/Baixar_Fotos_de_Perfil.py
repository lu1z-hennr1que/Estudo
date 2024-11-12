# Comando: pip install instaloader
import instaloader
# Crie uma instância do instalaoder
L = instaloader.Instaloader()

# Opcional, login e login de sessão
L.login('arts_tob1', '2626@dayanne_')
L.interactive_login('arts_tob1')
L.load_session_from_file('arts_tob1')



# Substítua 'arts_tob1' pelo nome de usuário do perfil que você deseja baixar
profile_name = ('alzenir_trindade')
# Baixe o perfil
try:
    profile = instaloader.Profile.from_username(L.context, profile_name)
except instaloader.exceptions.ProfileNotExistsException:
    print(f"O perfil '{profile_name}' não foi encontrado.")
    exit()
# Itere pelas postagens do perfil e baixe as fotos
for post in profile.get_posts():
    # Certifique-se de que a postagem tem fotos
    L.download_post(post, profile_name)
    print(f"Baixando: {post.url}")
print("Download concluído.")
