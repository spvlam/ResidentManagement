import { Card } from '@/app/ui/dashboard/cards';
import RevenueChart from '@/app/ui/dashboard/revenue-chart';
import LatestInvoices from '@/app/ui/dashboard/latest-invoices';
import { lusitana } from '@/app/ui/fonts';
import {
  fetchRevenue,
  fetchLatestInvoices,
  fetchCardData,
  fetchInvoiceById,
} from '@/app/lib/data';
import {getData} from '@/helper/data_helper/service'
import { useSearchParams } from 'react-router-dom';
export default async function Page() {
  // const [searchParams] = useSearchParams();
  // const userId = searchParams.get('userId');
  // console.log(userId)
  let revenue = await getData("http://localhost:8000/getRevanue");
  let latestInvoices = await getData("http://localhost:8000/family_detail/2489811");
  let person = await getData("http://localhost:8000/search/1803693")
  
 
  return (
    <main>
      <h1 className={`${lusitana.className} mb-4 text-xl md:text-2xl`}>
                              Dashboard
      </h1>
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">

      <Card title="Name" value={person.full_name} type="collected" />
        <Card title="Gender" value={person.gender} type="collected" />
        <Card title="Merried Status" value={person.married_status} type="pending" />
        <Card title="Dob" value={person.dob} type="invoices" />
        <Card
          title="Que_quan_tinh"
          value={person.que_quan_tinh}
          type="customers"
        />
        <Card
          title="Que_quan_huyen"
          value={person.que_quan_huyen}
          type="customers"
        />
        <Card
          title="Que_quan_xa"
          value={person.que_quan_xa}
          type="customers"
        />
        <Card
          title="family ID"
          value={person.family_id}
          type="customers"
        />

      </div>
      <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-4 lg:grid-cols-8">
        <RevenueChart revenue={revenue} />
        <LatestInvoices latestInvoices={latestInvoices} />
      </div>
    </main>
  );
}