// ./app/page.tsx
import ClientComponent from "@/components/ClientComponent";
import { fetchAccessToken } from "@humeai/voice";

export default async function Page() {
    console.log(process.env.NEXT_PUBLIC_HUME_API_KEY);
    console.log(process.env.NEXT_PUBLIC_HUME_SECRET_KEY);

    const accessToken = await fetchAccessToken({
        apiKey: String(process.env.NEXT_PUBLIC_HUME_API_KEY),
        secretKey: String(process.env.NEXT_PUBLIC_HUME_SECRET_KEY),
    });

    return <ClientComponent accessToken={accessToken} />;
}
